use std::io;

fn main() {
    let mut buf = String::new();
    io::stdin().read_line(&mut buf).unwrap();
    let rev = buf.split_whitespace().map(|x| x.parse::<i32>().unwrap()).map(|x| (x%10*100) + (x/100) + ((x - x/100*100)/10*10)).collect::<Vec<_>>();
    println!("{}", rev.iter().max().unwrap());
}