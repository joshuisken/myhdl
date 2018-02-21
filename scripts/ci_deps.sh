if [ "$CI_TARGET" == "iverilog" ]; then
  sudo apt-get -qq update
  sudo apt-get install iverilog
elif [ "$CI_TARGET" == "ghdl" ]; then
  url=$(curl -s https://api.github.com/repos/ghdl/ghdl/releases/latest | jq -r ".assets[] | select (.name | test (\"ubuntu14\"))| .browser_download_url")
  curl -Lo ghdl.deb $url
  sudo dpkg -i ghdl.deb
  sudo apt-get install -f
fi
