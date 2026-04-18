use std::{io, collections};

fn main() {
    let mut buf = String::new();
    io::stdin().read_line(&mut buf).unwrap();
    let mut usage: collections::HashMap<char, u32> = collections::HashMap::new();
    for i in buf.trim().to_uppercase().chars(){
        if usage.contains_key(&i){
            *usage.get_mut(&i).unwrap() += 1;
        }else{
            usage.insert(i, 1);
        }
    }
    let max = usage.iter().max_by_key(|&(_,y)| y).unwrap();
    if usage.values().filter(|x| *x == max.1).count() == 1{
        println!("{}", max.0);
    }else{
        println!("?");
    }
}