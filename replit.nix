{ pkgs }: {
    deps = [
        pkgs.bashInteractive
        pkgs.python310.out
        pkgs.python310Packages.pip.out
    ];
}
