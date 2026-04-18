use std::io;

fn main() {
    let mut x = String::new();
    io::stdin().read_line(&mut x).unwrap();
    x = x.trim().to_owned();
    let res = x.parse::<u32>().unwrap();
    let mut x = res;
    let mut i = 1;
    loop{
        //let c = x.chars().map(|r| r.to_digit(10).unwrap()).collect::<Vec<u32>>();
        let f = x / 10;
        let b = x % 10;
        x = b * 10 + ((f + b) % 10);
        //x = format!("{}{}", c.last().unwrap(), s.to_string().chars().last().unwrap()).trim_start_matches("0").to_owned();
        if x == res{
            println!("{}", i);
            break;
        }
        i+=1;
    }
}