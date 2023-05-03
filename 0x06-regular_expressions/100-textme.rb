#!/usr/bin/env ruby
#Text me
from = ARGV[0].scan(/from:([^\]]+)/)
to = ARGV[0].scan(/to:([^\]]+)/)
flags = ARGV[0].scan(/flags:([^\]]+)/)
x = from.size
i = 0
while i < x
  puts "#{from[i][0]},#{to[i][0]},#{flags[i][0]}"
  i = i + 1
end

