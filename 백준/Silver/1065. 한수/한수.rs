use std::io;

fn check(x: i32) -> bool{
    if x < 100{
        true
    }else{
        let x = x.to_string().chars().map(|x| x.to_digit(10).unwrap() as i32).collect::<Vec<i32>>();
        if x[0] - x[1] == x[1] - x[2]{
            true
        }else{
            false
        }
    }
}

fn main() {
    let mut inp = String::new();
    io::stdin().read_line(&mut inp).unwrap();
    let mut c = 0;
    for i in 1..inp.trim_end().parse::<i32>().unwrap()+1{
        if check(i){
            c += 1;
        }
    }
    println!("{}", c);
}
