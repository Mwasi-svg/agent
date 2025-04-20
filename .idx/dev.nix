{ pkgs, ... }: {
  channel = "stable-24.05";

  packages = [
    (pkgs.python312.withPackages (ps: with ps; [
      pip
      google-generativeai
    ]))
    pkgs.python-launcher
    # pkgs.nodejs_20
    # pkgs.nodePackages.nodemon
  ];

  env = {};

  idx = {
    extensions = [];

    previews = {
      enable = true;
      previews = {};
    };

    workspace = {
      onCreate = {};
      onStart = {};
    };
  };
}
