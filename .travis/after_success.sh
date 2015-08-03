OUT="$(mktemp)"
echo $SSH_key > $OUT
ssh -o "StrictHostKeyChecking no" www.whatdayisitin.nz -l $SSH_USER -i $OUT
cd /var/www/whatdayisitinnz/whatdayisitinnz
git pull
virtualenv whatdayisitinnz/venv
source whatdayisitinnz/venv/bin/activate
pip install -r requirements.txt
deactivate
service apache2 restart