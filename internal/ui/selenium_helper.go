//go:build ui
// +build ui

package ui

import (
	"fmt"
	"os"
	"time"

	"github.com/tebeka/selenium"
)

// NewWebDriver connects to a Selenium server (e.g., chromedriver) and returns a WebDriver
// It reads SELENIUM_URL (default: http://127.0.0.1:9515) and SELENIUM_PORT (default: 9515).
func NewWebDriver() (selenium.WebDriver, func(), error) {
	seleniumURL := os.Getenv("SELENIUM_URL")
	if seleniumURL == "" {
		seleniumURL = "http://127.0.0.1:9515"
	}

	caps := selenium.Capabilities{"browserName": "chrome"}

	// Connect to the WebDriver instance running at seleniumURL
	wd, err := selenium.NewRemote(caps, seleniumURL)
	if err != nil {
		return nil, nil, fmt.Errorf("unable to connect to selenium at %s: %w", seleniumURL, err)
	}

	// small implicit wait for element searches
	_ = wd.SetImplicitWaitTimeout(5 * time.Second)

	cleanup := func() {
		_ = wd.Quit()
	}

	return wd, cleanup, nil
}
