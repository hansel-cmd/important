from unittest.mock import Mock


"""
Replace inconvenient collaborators
- Dummy
- Stub
- Fake

Ensure interactions are correct
- Spy
- Mock
"""

class Alarm:

    def __init__(self, sensor = None):
        self._low_pressure_threshold = 17
        self._high_pressure_threshold = 21
        self._sensor = sensor or Sensor()
        self._is_alarm_on = False

    def check(self):
        pressure = self._sensor.sample_pressure()
        if pressure is None:
            return
        
        if pressure < self._low_pressure_threshold > pressure \
            or pressure > self._high_pressure_threshold:
            self._is_alarm_on = True

    @property
    def is_alarm_on(self):
        return self._is_alarm_on


class Sensor:

    def sample_pressure(self):
        pass

    def other(self):
        pass

    def other_methods(self):
        pass

"""Using Stubs..."""
class StubSensor:

    # The only method that Alarm() needs.
    def sample_pressure(self):
        return 15

"""
Creates own Stub Class to mimick original sensor.
"""
def test_low_pressure_activates_alarm():
    alarm = Alarm(sensor = StubSensor())
    alarm.check()
    assert alarm.is_alarm_on

"""
Mock the original sensor to create a stub object.
Assign a return value to the only function that Alarm()
needs.
"""
def test_normal_pressure_alarm_stays_off():
    stub_sensor = Mock(Sensor)
    stub_sensor.sample_pressure.return_value = 19
    alarm = Alarm(stub_sensor)
    alarm.check()
    assert not alarm.is_alarm_on

"======================================================="
import io
import html as html_converter

"""Using Fakes..."""
class HtmlPagesConverter:

    def __init__(self, open_file):
        self.open_file = open_file
        self._find_page_breaks()

    def _find_page_breaks(self):
        self.breaks = [0]
        while True:
            line = self.open_file.readline()
            if not line:
                break
            if "PAGE_BREAK" in line:
                self.breaks.append(self.open_file.tell())
        self.breaks.append(self.open_file.tell())

    def get_html_page(self, page):
        page_start = self.breaks[page]
        page_end = self.breaks[page + 1]
        html = ""
        self.open_file.seek(page_start)
        while self.open_file.tell() != page_end:
            line = self.open_file.readline()
            if "PAGE_BREAK" in line:
                continue
            line = line.rstrip()
            html += html_converter.escape(line, quote = True)
            html += "<br />"
        return html

"""
Instead of passing a real text file, we use io.StringIO()
since it has the same implementation as texts.

We fake it.
"""
def test_convert_quotes():
    fake_file = io.StringIO("quote: ' ")
    converter = HtmlPagesConverter(open_file=fake_file)
    converted_text = converter.get_html_page(0)
    assert converted_text == "quote: &#x27;<br />"

def test_access_second_page():
    fake_file = io.StringIO("""\
page one
PAGE_BREAK
page two
PAGE_BREAK
page three
""")
    converter = HtmlPagesConverter(open_file = fake_file)
    converter_text = converter.get_html_page(1)
    assert converter_text == "page two<br />"

"======================================================="

"""
Passing Dummy or None in place of a collaborator.
Give an alternative to something.
"""

"Using Dummy..."
def fizzbuzz(n, additional_rule):
    answer = ""
    rules = {3: "Fizz", 5: "Buzz"}
    if additional_rule:
        rules.update(additional_rule)
    for divisor in sorted(rules.keys()):
        if n % divisor == 0:
            answer += rules[divisor]
    if not answer:
        answer = str(n)
    return answer

def test_fizzbuzz():
    assert fizzbuzz(2, None) == '2'
    assert fizzbuzz(4, None) == '4'
    assert fizzbuzz(5, None) == 'Buzz'
    assert fizzbuzz(3, None) == 'Fizz'
    assert fizzbuzz(15, None) == 'FizzBuzz'
    assert fizzbuzz(8, {2: 'HELLO'}) == 'HELLO'

"======================================================="

"""
Spy will make sure that a specific method is ran.
"""

"""Using Spy..."""
import random
class MyService:

    def __init__(self, sso_registry):
        self.sso_registry = sso_registry

    def handle(self, request, sso_token):
        if self.sso_registry.is_valid(sso_token):
            return Response(f"Hello, {request.name}!")
        return Response("Please sign in")
    
class Request:
    def __init__(self, name):
        self.name = name

class Response:
    def __init__(self, text):
        self.text = text

class SingleSignOnRegistry:
    def register_new_session(self, credentials):
        pass

    def is_valid(self, token):
        pass

    def unregister(self, token):
        pass

class SSOToken:
    def __init__(self):
        self.id = random.randrange(10000)
    
    def __eq__(self, other):
        return self.id == other.id
    
    def __repr__(self):
        return str(self.id)

"""A stub doesnt care if the method is run or not. 
It only cares about the output at the end
"""
def test_hello_name():
    stub_sso_registry = Mock(SingleSignOnRegistry)
    service = MyService(stub_sso_registry)
    response = service.handle(Request("Katarina"), SSOToken())
    assert response.text == "Hello, Katarina!"

"""A spy will make sure that a method is ran."""
def test_single_sign_on():
    spy_sso_registry = Mock(SingleSignOnRegistry)
    service = MyService(spy_sso_registry)
    token = SSOToken
    service.handle(Request("Katarina"), token)
    spy_sso_registry.is_valid.assert_called_with(token)

def test_single_sign_on_with_invalid_token():
    spy_sso_registry = Mock(SingleSignOnRegistry)
    spy_sso_registry.is_valid.return_value = False
    service = MyService(spy_sso_registry)
    token = SSOToken
    response = service.handle(Request("Katarina"), token)
    spy_sso_registry.is_valid.assert_called_with(token)
    assert response.text == "Please sign in"

"======================================================="

"""Using Mock..."""
def confirm_token(correct_token):
    def is_valid(actual_token):
        if actual_token != correct_token:
            raise ValueError("Wrong token received")
    return is_valid

def test_single_sign_on_receives_correct_token():
    mock_sso_registry = Mock(SingleSignOnRegistry)
    correct_token = SSOToken()
    mock_sso_registry.is_valid = Mock(side_effect = 
                                    confirm_token(correct_token))
    service = MyService(mock_sso_registry)
    service.handle(Request("Katarina"), correct_token)
    mock_sso_registry.is_valid.assert_called()