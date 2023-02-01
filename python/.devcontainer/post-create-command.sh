#!/bin/bash
cd backend
rm -rf ./.venv
python -m venv .venv
chmod +x ./.venv/bin/activate
./.venv/bin/activate

./.venv/bin/pip3 install -r requirements.txt

cd -

cd frontend
npm install
cd -

