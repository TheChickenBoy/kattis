use std::io::{BufReader};

fn main() -> io::Result<()> {
    let input = BufReader::new(io::stdin());
    // let mut buffer = String::new();
    // let stdin = io::stdin();
    // let mut handle = stdin.lock();

    // handle.read_to_string(&mut buffer)?;
    println!("Thank you, {}, and farewell!", input);
    Ok(())
}

use std::io;
use std::io::prelude::*;

fn main() {
    //print_single_line("Please enter your forename: ");
    //let forename = read_line_iter();
    println!("Thank you, {}, and farewell!", read_line_iter());
}  
fn read_line_iter() -> String {
    let stdin = io::stdin();
    
    let input = stdin.lock().lines().next();
    input.expect("No lines in buffer").expect("Failed to read line").trim().to_string()
}
