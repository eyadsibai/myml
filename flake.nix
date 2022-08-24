{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, utils }:
    let
      out = system:
        let pkgs = nixpkgs.legacyPackages."${system}";
        in
        {

          devShell = pkgs.mkShell {
            buildInputs = with pkgs; [
              nixpkgs-fmt
              poetry
              (pkgs.poetry2nix.mkPoetryEnv {
                # inherit python;
                projectDir = ./.;
                editablePackageSources = {
                  my-app = ./src;
                };
                preferWheels = true;

              })
            ];
          };

        };
    in
    with utils.lib; eachSystem defaultSystems out;

}
