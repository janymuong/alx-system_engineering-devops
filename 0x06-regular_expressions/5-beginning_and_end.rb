#!/usr/bin/env ruby

# regex for 'text-given':begin=h, end=n
puts ARGV[0].scan(/^h.n$/).join
