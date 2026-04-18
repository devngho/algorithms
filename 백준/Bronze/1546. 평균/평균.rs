use std::{io, cmp::Ordering};

fn main() {
    let mut inp = String::new();
    io::stdin().read_line(&mut inp).unwrap();
    inp.clear();
    io::stdin().read_line(&mut inp).unwrap();
    let scores = inp.trim().split_whitespace().map(|x| x.parse::<f64>().unwrap()).collect::<Vec<f64>>();
    let max = *scores.iter().max_by(|a, b| a.partial_cmp(b).unwrap_or(Ordering::Equal)).unwrap();
    let mut n_scores: Vec<f64> = Vec::new();
    scores.iter().for_each(|x| n_scores.push(x / max * 100 as f64));
    println!("{}", n_scores.iter().sum::<f64>() / ((n_scores.len()) as f64))
}
