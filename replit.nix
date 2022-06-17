{ pkgs }: {
    deps = [
        pkgs.bashInteractive
        pkgs.python310.out
        pkgs.python10Packages.pip.out
    ];
}
