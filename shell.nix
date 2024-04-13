let
  # Fetch the nixpkgs-unstable channel
  nixpkgsUnstable = fetchTarball {
    url = "https://github.com/NixOS/nixpkgs/archive/nixpkgs-unstable.tar.gz";
    # Optionally, you can specify a SHA-256 hash for the tarball for reproducibility
    # sha256 = "<hash>";
  };

  # Import the fetched nixpkgs-unstable channel
  pkgs = import nixpkgsUnstable { };

in pkgs.mkShell {
  packages = [
    (pkgs.python3.withPackages
      (python-pkgs: with python-pkgs; [ gradio pandas psycopg2 ]))
  ];
}
# let pkgs = import <nixpkgs> { };
# in pkgs.mkShell {
#   packages = [
#     pkgs.openai-full
#     (pkgs.python3.withPackages
#       (python-pkgs: [ python-pkgs.gradio python-pkgs.openai ]))
#   ];
# }
