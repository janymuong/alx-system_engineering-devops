#!/usr/bin/env ruby

# regex for 'School' - a single command-line arg
puts ARGV[0].scan(/\bSchool\b/).join
