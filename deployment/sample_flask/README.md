### Docker Run

```powershell
Set-Alias -Name which -Value Get-Command

conda create -n 3.10.14 python=3.10.14
conda activate 3.10.14

pip install pipenv 
which python

pipenv install --python C:\anaconda3\envs\3.10.14\python.exe

pipenv install flask 
pipenv install tensorflow
pipenv install python-dotenv
pipenv install gunicorn

```

```bash
docker build . -t test_flask

docker run -p 3000:8000 test_flask

docker run -p 3000:8000 --env PORT=8000 test_flask
```