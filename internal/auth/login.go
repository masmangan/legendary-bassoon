package auth

import (
	"bytes"
	"encoding/json"
	"fmt"
	"net/http"
	"os"
)

type LoginResponse struct {
	Status string `json:"status"`
}

func Login(client *http.Client, username, password string) error {
	baseURL := os.Getenv("ORANGEHRM_BASE_URL")
	if baseURL == "" {
		return fmt.Errorf("ORANGEHRM_BASE_URL not set")
	}
	url := fmt.Sprintf("%s/web/index.php/auth/validate", baseURL)

	payload := map[string]string{
		"username": username,
		"password": password,
	}
	body, _ := json.Marshal(payload)

	req, err := http.NewRequest("POST", url, bytes.NewBuffer(body))
	if err != nil {
		return err
	}
	req.Header.Set("Content-Type", "application/json")

	resp, err := client.Do(req)
	if err != nil {
		return err
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		return fmt.Errorf("login failed: status %d", resp.StatusCode)
	}

	return nil
}
