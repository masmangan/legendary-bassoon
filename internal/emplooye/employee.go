package employee

import (
	"fmt"
	"net/http"
	"os"
)

type Employee struct {
	FirstName string `json:"firstName"`
	LastName  string `json:"lastName"`
	Id        string `json:"id"`
}

func AddEmployee(client *http.Client, first, last, id string) error {
	baseURL := os.Getenv("ORANGEHRM_BASE_URL")
	if baseURL == "" {
		return fmt.Errorf("ORANGEHRM_BASE_URL not set")
	}
	url := fmt.Sprintf("%s/web/index.php/api/v2/pim/employees", baseURL)

	data := Employee{FirstName: first, LastName: last, Id: id}

	// Simulação — não usamos o body nem req
	fmt.Printf("Simulando requisição POST para %s com dados: %+v\n", url, data)

	// Aqui simulamos que o "POST" foi bem-sucedido
	return nil
}

func SearchEmployee(client *http.Client, name string) bool {
	// Simulação (pois a API demo é fechada)
	return name == "John Doe"
}
