#!/usr/bin/env ruby

# regex for 'text-given': zero or more
puts ARGV[0].scan(/\bhbt*n\b/).join
