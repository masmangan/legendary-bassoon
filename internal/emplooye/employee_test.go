package employee

import (
	"os"
	"testing"

	"orangehrm-tests/internal/auth"
	"orangehrm-tests/internal/utils"

	"github.com/joho/godotenv"
	"github.com/stretchr/testify/assert"
)

func TestEmployeeJourney(t *testing.T) {
	err := godotenv.Load("../../.env")
	if err != nil {
		t.Fatal("Error loading .env file")
	}
	client := utils.NewClient()

	// login
	loginErr := auth.Login(client, os.Getenv("ORANGEHRM_USER"), os.Getenv("ORANGEHRM_PASS"))
	assert.NoError(t, loginErr)

	// adicionar funcionário
	err = AddEmployee(client, "John", "Doe", "12345")
	assert.NoError(t, err)

	// buscar funcionário
	found := SearchEmployee(client, "John Doe")
	assert.True(t, found)
}
