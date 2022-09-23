# Console Kata Anagrams
This is a console app that use Kata Anagrams Library.

## Set Up
Should have installed Python version greater than or equal 3.7.

1. Clone the repository.

2. Create ```env``` folder using following command:
```bash
$ py -m venv --clear --symlinks env
```

3. Execute activate script:
```bash
$ "env/Scripts/activate"
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Run app:
```bash
$ py main.py <file_path> <mode>
```

Examples:
```bash
# Normal Mode
$ py main.py "./assets/wordslist.txt"

# Advanced Mode
$ py main.py "./assets/wordslist.txt" --advanced
```