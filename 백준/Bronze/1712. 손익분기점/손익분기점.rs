use std::io;

fn main() {
    let mut buf = String::new();
    io::stdin().read_line(&mut buf).unwrap();
    let buf: Vec<_> = buf.split_whitespace().map(|x| x.parse::<i64>().unwrap()).collect();
    if buf[1] < buf[2]{
        println!("{}",  buf[0] / (buf[2] - buf[1]) + 1)
    }else{
        println!("-1")
    }
}
