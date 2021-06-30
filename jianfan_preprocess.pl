#!/usr/bin/perl
use strict;
use utf8;

use File::Basename;
use Getopt::Long qw(:config posix_default no_ignore_case gnu_compat);

my $char_data = {    
    "jianfan" => {
        "file" => "jianfan_all.txt",
        "data" => {}
    },
    "fanjian" => {
        "file" => "fanjian_all.txt",
        "data" => {}
    }
};

sub main {
    $| = 1;
    my %opts;
    Getopt::Long::GetOptions(
        \%opts,
        "reverse"
        );

    my $direction = $opts{"reverse"} ? "fanjian" : "jianfan";
    
    my $script_dir = dirname(__FILE__);

    for my $d(keys %{$char_data}) {
        open my $in, "<:utf8", "$script_dir/$char_data->{$d}->{'file'}" or die "Cannot open file: $script_dir/$char_data->{$d}->{'file'}";
        while (<$in>) {
            chomp;
            my @F = split /\t/;
            die "Illegal file format: $char_data->{$d}->{'file'}:$. $_" if length($F[0]) != 1 or length($F[1]) < 1 or scalar(@F) > 2;
            $char_data->{$d}->{"data"}->{$F[0]} = [split(//, $F[1])];
        }
    }

    binmode STDIN, ':utf8';
    binmode STDOUT, ':utf8';
    my $data_ref = $char_data->{$direction}->{"data"};
    while (<STDIN>) {
        chomp;
        s{ }{\x{e000}}g;
        print join(" ", map { exists $data_ref->{$_} ? (scalar(@{$data_ref->{$_}}) > 1 ? "[".join("|", @{$data_ref->{$_}})."]" : $data_ref->{$_}->[0]) : $_; } split(//, $_))."\n";
    }
}
    
if ($0 eq __FILE__) {
    main();
}
