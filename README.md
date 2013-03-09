Tests:
```
class SimpleTest(TestCase):
  _multiprocess_shared_ = True 
  
  def test_sleep_10(self):
    time.sleep(10)

  def test_sleep_5(self):
    time.sleep(5)
```

Results:
```
python manage.py test --processes=4 --process-timeout=60 --with-progressive  0.32s user 0.11s system 2% cpu 15.456 total
python manage.py test --processes=4 --process-timeout=60  0.47s user 0.45s system 8% cpu 10.600 total
```
