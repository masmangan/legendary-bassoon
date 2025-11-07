//go:build ui
// +build ui

package ui

import (
	"os"
	"strings"
	"testing"
	"time"

	"github.com/joho/godotenv"
	"github.com/stretchr/testify/assert"
	"github.com/tebeka/selenium"
)

func TestLoginUI(t *testing.T) {
	// Load environment
	err := godotenv.Load("../../.env")
	if err != nil {
		t.Fatal("Error loading .env file for UI tests")
	}

	wd, cleanup, err := NewWebDriver()
	if err != nil {
		// If webdriver not available, skip UI tests
		t.Skipf("Skipping UI tests: %v", err)
	}
	defer cleanup()

	baseURL := os.Getenv("ORANGEHRM_BASE_URL")
	if baseURL == "" {
		t.Fatal("ORANGEHRM_BASE_URL not set")
	}

	if err := wd.Get(baseURL); err != nil {
		t.Fatalf("failed to open base url: %v", err)
	}

	// helper to try find element by several strategies
	findElement := func() (selenium.WebElement, error) {
		// try by name
		if el, e := wd.FindElement(selenium.ByName, "username"); e == nil {
			return el, nil
		}
		// try by id common for some versions
		if el, e := wd.FindElement(selenium.ByID, "txtUsername"); e == nil {
			return el, nil
		}
		// try css selector
		if el, e := wd.FindElement(selenium.ByCSSSelector, "input[name='username']"); e == nil {
			return el, nil
		}
		return nil, selenium.ErrNoSuchElement
	}

	usernameEl, err := findElement()
	if err != nil {
		t.Fatalf("could not find username field: %v", err)
	}

	// password field
	var passwordEl selenium.WebElement
	if el, e := wd.FindElement(selenium.ByName, "password"); e == nil {
		passwordEl = el
	} else if el, e := wd.FindElement(selenium.ByID, "txtPassword"); e == nil {
		passwordEl = el
	} else if el, e := wd.FindElement(selenium.ByCSSSelector, "input[name='password']"); e == nil {
		passwordEl = el
	} else {
		t.Fatalf("could not find password field: %v", err)
	}

	// enter credentials
	if err := usernameEl.Clear(); err != nil {
		// ignore clear errors
	}
	if err := usernameEl.SendKeys(os.Getenv("ORANGEHRM_USER")); err != nil {
		t.Fatalf("failed to send username: %v", err)
	}
	if err := passwordEl.SendKeys(os.Getenv("ORANGEHRM_PASS")); err != nil {
		t.Fatalf("failed to send password: %v", err)
	}

	// find and click submit
	var submit selenium.WebElement
	if el, e := wd.FindElement(selenium.ByCSSSelector, "button[type='submit']"); e == nil {
		submit = el
	} else if el, e := wd.FindElement(selenium.ByID, "btnLogin"); e == nil {
		submit = el
	} else if el, e := wd.FindElement(selenium.ByCSSSelector, "input[type='submit']"); e == nil {
		submit = el
	} else {
		t.Fatalf("could not find submit button")
	}

	if err := submit.Click(); err != nil {
		t.Fatalf("failed to click submit: %v", err)
	}

	// wait for title or url change to indicate success
	success := false
	timeout := time.Now().Add(10 * time.Second)
	for time.Now().Before(timeout) {
		title, _ := wd.Title()
		if strings.Contains(strings.ToLower(title), "dashboard") {
			success = true
			break
		}
		url, _ := wd.CurrentURL()
		if strings.Contains(strings.ToLower(url), "dashboard") {
			success = true
			break
		}
		time.Sleep(500 * time.Millisecond)
	}

	assert.True(t, success, "expected to reach dashboard after login")
}
