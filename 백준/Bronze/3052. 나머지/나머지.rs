use std::io;

fn main() {
    let mut used: Vec<i32> = Vec::new();
    let mut res = 0;
    let mut buf = String::new();
    for _ in 0..10 {
        io::stdin().read_line(&mut buf).unwrap();
        let i = buf.trim_end().parse::<i32>().unwrap() % 42;
        buf.clear();
        if !used.contains(&i){
            res += 1;
            used.push(i);
        }
    }
    println!("{}", res);
}
