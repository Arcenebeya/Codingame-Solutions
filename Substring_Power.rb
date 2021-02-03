s=gets
p (0..31).map{|i|((s[(2**i).to_s]?1:0)*2**i)}.max
