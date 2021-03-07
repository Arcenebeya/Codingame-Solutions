
n = gets.to_i
x = gets.split.map(&:to_i).map{|i| i.digits.sum}

p x.sum
