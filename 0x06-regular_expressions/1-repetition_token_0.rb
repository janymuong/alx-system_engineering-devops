#!/usr/bin/env ruby

# regex for 'text-given'
puts ARGV[0].scan(/\bhbt{2,5}n\b/).join
