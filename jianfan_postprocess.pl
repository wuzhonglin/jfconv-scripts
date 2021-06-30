#!/usr/bin/perl
use strict;
use utf8;

sub main {
    $| = 1;
    binmode STDIN, ':utf8';
    binmode STDOUT, ':utf8';
    while (<STDIN>) {
        chomp;
        my @words = split / /;
        my $t = join("", @words)."\n";
        $t =~ s{\x{e000}}{ }g;
        print $t;
    }
}
    
if ($0 eq __FILE__) {
    main();
}
