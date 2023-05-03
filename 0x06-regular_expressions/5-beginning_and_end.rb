#!/usr/bin/env ruby

# regex for 'text-given':begin=h, end=n
puts ARGV[0].scan(/\bh[a-z0-9][^t]*n\b/).join
