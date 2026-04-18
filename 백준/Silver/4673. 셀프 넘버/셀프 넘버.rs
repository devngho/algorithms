fn main() {
    let mut not_self_numbers: Vec<u32> = Vec::new();
    for i in 1..10000{
        not_self_numbers.push(i + i.to_string().chars().map(|x| x.to_digit(10).unwrap()).sum::<u32>());
    }
    for i in 1..10000 {
        if !not_self_numbers.contains(&i){
            println!("{}", i);
        }
    }
}