sudo apt update
sudo apt install kitty-terminfo
ls
git clone git@github.com:itc-n26011/PG_Basics.git
clear
git status
ls
rm -rf PG_Basics/
ls
git clone git@github.com:itc-n26011/PG_Basics.git .
la
git clone git@github.com:itc-n26011/PG_Basics.git /tmp/PG_Basics
cp -a /tmp/PG_Basics/. ~/ 
rm -rf /tmp/PG_Basics
ls
git status
cat > ~/.gitignore <<'EOF'
.bash_logout
.bashrc
.profile
.cache/
.ssh/
.sudo_as_admin_successful
EOF

git add .gitignore
git commit -m "Add gitignore"
git config --global user.email "n26011@std.it-college.ac.jp"
git config --global user.name "n26011"
cat > ~/.gitignore <<'EOF'
.bash_logout
.bashrc
.profile
.cache/
.ssh/
.sudo_as_admin_successful
EOF

git add .gitignore
git commit -m "Add gitignore"
git brach -a
git branch -a
git switch CH02
git switch CH03
git switch CH04
git switch CH05
git switch CH06
git switch CH07
git switch CH08
clear
ls
git branch main
git switch main
git branch
git push origin main
clear
ls
cat README.md 
exit
