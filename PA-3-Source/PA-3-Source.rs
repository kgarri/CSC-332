use core::fmt;
use std::{
    collections::HashMap,
    fs::File,
    io::{self, prelude::*, Write},
    path::Path,
    time::Instant,
};
/*print_timeit is a rust macro that takes in a function as an argument with args...
that is then run its result is obtained
then it prints out the time it took to get that result in nanoseconds */
macro_rules! print_timeit {
    ($func:expr,$($arg:expr),+) =>{
        {
            let before = Instant::now();
            let result = $func($($arg),+);
            let elasped = before.elapsed().as_nanos();
            println!("Your result {} took {} nanoseconds",result,elasped)
     }
    };
}

macro_rules! timeit {
    ($func:expr,$($arg:expr),+) => {
        {
            let before= Instant::now();
                $func($($arg),+);
            let elapsed = before.elapsed().as_nanos();
            elapsed
        }

    };
}

struct Fibonacci {
    n: i64,
    result: i64,
    rec_time: u128,
    dp_time: u128,
    n_sq_time: f64,
    dp_rec_time: f64,
}

impl Fibonacci {
    fn new(n: i64, result: i64, rec_time: u128, dp_time: u128) -> Fibonacci {
        let f_n: f64 = n as f64;
        let n_sq_time: f64 = f_n.exp2() / f_n;
        let f_rec_time: f64 = rec_time as f64;
        let f_dp_time: f64 = dp_time as f64;
        let dp_rec_time: f64 = f_rec_time / f_dp_time;

        Fibonacci {
            n,
            result,
            rec_time,
            dp_time,
            n_sq_time,
            dp_rec_time,
        }
    }
}

impl fmt::Display for Fibonacci {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(
            f,
            "{}, {}, {}, {}, {:+.0e}, {:+.0e}",
            self.n, self.result, self.rec_time, self.dp_time, self.n_sq_time, self.dp_rec_time
        )
    }
}

/*rec_fib should obviously be the recursive fibonacci function
   it has two base cases when n=1 return 0
   and when n = 2 return 1
   else
   call two versions of itself one with n-1 as the input another with n-2 as the input
*/
fn rec_fib(n: i64) -> i64 {
    if n == 1 {
        return 1;
    }
    if n == 2 {
        return 1;
    }
    return rec_fib(n - 1) + rec_fib(n - 2);
}

/* this is obviously the dynamic programming fibonacci, as shown by the utilization of a cache to utilize memozation
   the HashMap is a dictonary of values that are used to find if a value has already been calculated, it actually changes the cache in place
   as shown by the mutable type also being a reference
   it either returns the cached value or the result of a recursive call of the dp_fib variety
*/
fn dp_fib(n: i64, cache: &mut HashMap<i64, i64>) -> i64 {
    if cache.contains_key(&n) {
        return cache[&n];
    }
    let result = dp_fib(n - 1, cache) + dp_fib(n - 2, cache);
    cache.insert(n, result);
    return result;
}

/*get_num() is an atomic function that is meant to get the user input of the index value they want returned from the fibonacci sequence
this is because it is utlized in multiple places and just want to ensure that the actual value inputed is a number
else it will return -1 where the main does further error checking
*/
fn get_num() -> i64 {
    let mut num = String::new();
    println!("Please input your number");
    io::stdin()
        .read_line(&mut num)
        .expect("Failed to read line");
    let new_num: Result<i64, _> = num.trim().parse();
    match new_num {
        Ok(number) => return number,
        Err(_) => return -1,
    }
}

fn get_fibs(nums: [i64; 7]) -> Vec<Fibonacci> {
    let mut map: HashMap<i64, i64> = HashMap::from([(1, 1), (2, 1)]);
    let mut fib_list: Vec<Fibonacci> = Vec::new();
    for n in nums.iter() {
        let fibnum = dp_fib(*n, &mut map);
        let time1 = timeit!(rec_fib, *n);
        let time2 = timeit!(dp_fib, *n, &mut map);
        let fib = Fibonacci::new(*n, fibnum, time1, time2);
        fib_list.push(fib);
    }
    return fib_list;
}

fn save_to_file<T: ToString>(headers: Vec<&str>, items: Vec<T>, path: &Path) {
    let display = path.display();
    let mut file = match File::create(&path) {
        Err(why) => panic!("Couldn't create {}: {}", display, why),
        Ok(file) => file,
    };

    writeln!(file, "{}", headers.join(",")).expect("Failed to write to file");
    for item in items.iter() {
        writeln!(file, "{}", item.to_string()).expect("Failed to write to file");
    }
    println!("File {} has been generated", display);
}

fn pause() {
    let mut stdin = io::stdin();
    let mut stdout = io::stdout();

    write!(stdout, "Press any key to exit uwu").unwrap();
    stdout.flush().unwrap();

    let _ = stdin.read(&mut [0u8]).unwrap();
}

/*
main is where the main loop of the program is pretty self explainatory
 */
fn main() {
    let mut map: HashMap<i64, i64> = HashMap::from([(1, 1), (2, 1)]); //a map containing the first two values of the fibonacci sequence
    let mut cont_var = true; //cont_var stands for continue variable that determines if the loop should continue or not
    let headers = vec![
        "n",
        "F(n)",
        "T1: Recrusive Time (ns)",
        "T2: DP Time (ns)",
        "Value of 2^n/n",
        "Value of T1/T2",
    ];
    let path = Path::new("Fibonacci_Time.csv");
    println!("Welcome to the Fibonacci Comparision App");
    while cont_var {
        //esentially a while true loop, pretty self explainatory
        println!("\nPlease select one of the following uwu <3:");
        println!("[1]: Recrussive Fibonacci");
        println!("[2]: Dynamic Programming Fibonacci");

        let mut input = String::new(); // user input
        let mut keep_going = String::new(); //more user input

        io::stdin() //getting user input to determin which fibonacci
            .read_line(&mut input)
            .expect("Failed to read line");

        //case to determine if the user gave valid inputs
        match input.trim().parse().expect("Failed to get integer") {
            1 => {
                let number = get_num();
                if number == -1 {
                    println!("Failed to get number")
                } else {
                    print_timeit!(rec_fib, number);
                }
            }
            2 => {
                let number = get_num();
                if number == -1 {
                    println!("Failed to get number")
                } else {
                    print_timeit!(dp_fib, number, &mut map);
                }
            }
            _ => println!("Invalid input recived"),
        }

        println!("Would you wish to continue  (Y/N)");

        io::stdin()
            .read_line(&mut keep_going)
            .expect("Failed to read line");

        // simple if statment to determine if the user wants to exit the program
        if keep_going.trim().to_lowercase() == String::from("y") {
            cont_var = true;
        } else {
            cont_var = false;
        }
    }
    println!("Thank you for using our application uwu <3");

    println!("\n***Generating CSV File***");
    let nums: [i64; 7] = [10, 12, 15, 20, 23, 25, 30];
    let fib_list = get_fibs(nums);
    for fib in fib_list.iter() {
        println!("{}", fib.to_string());
    }
    save_to_file(headers, fib_list, path);
    println!("***File has Completed Generation***");
    pause();
}
