ssh www.whatdayisitin.nz -l $SSH_USER -Q "$SSH_KEY"
cd /var/www/whatdayisitinnz/whatdayisitinnz
git pull
virtualenv whatdayisitinnz/venv
source whatdayisitinnz/venv/bin/activate
pip install -r requirements.txt