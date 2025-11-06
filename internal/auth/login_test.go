package auth

import (
	"os"
	"testing"

	"orangehrm-tests/internal/utils"

	"github.com/joho/godotenv"
	"github.com/stretchr/testify/assert"
)

func TestBuildLoginPayload(t *testing.T) {
	payload := map[string]string{
		"username": "Admin",
		"password": "admin123",
	}

	assert.Equal(t, "Admin", payload["username"])
	assert.Equal(t, "admin123", payload["password"])
}

func TestLoginIntegration(t *testing.T) {
	err := godotenv.Load("../../.env")
	if err != nil {
		t.Fatal("Error loading .env file")
	}
	client := utils.NewClient()

	user := os.Getenv("ORANGEHRM_USER")
	pass := os.Getenv("ORANGEHRM_PASS")

	loginErr := Login(client, user, pass)
	assert.NoError(t, loginErr)
}
