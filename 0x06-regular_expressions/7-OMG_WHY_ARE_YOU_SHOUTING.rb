#!/usr/bin/env ruby

# regex for UPPERCASE char-seq
puts ARGV[0].scan(/[A-Z]*/).join
