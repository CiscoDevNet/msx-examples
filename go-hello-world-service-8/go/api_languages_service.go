/*
 * Hello World Service
 *
 * Hello World service with support for multiple languages.
 *
 * API version: 1
 * Generated by: OpenAPI Generator (https://openapi-generator.tech)
 */

package openapi

import (
	"context"
	"net/http"
	"errors"
)

// StubLanguage is a sample language for this example
var StubLanguage = Language{
	Id:          "20f329ac-123f-48f0-917d-a70497cfd22a",
	Name:        "Esperanto",
	Description: "Esperanto is a constructed auxiliary language. Its creator was L. L. Zamenhof, a Polish eye doctor.",
}

// LanguagesApiService is a service that implents the logic for the LanguagesApiServicer
// This service should implement the business logic for every endpoint for the LanguagesApi API. 
// Include any external packages or services that will be required by this service.
type LanguagesApiService struct {
}

// NewLanguagesApiService creates a default api service
func NewLanguagesApiService() LanguagesApiServicer {
	return &LanguagesApiService{}
}

// CreateLanguage - Creates a new langauge.
func (s *LanguagesApiService) CreateLanguage(ctx context.Context, language Language) (ImplResponse, error) {
	// TODO - update CreateLanguage with the required logic for this service method.
	// Add api_languages_service.go to the .openapi-generator-ignore to avoid overwriting this service implementation when updating open api generation.

	//TODO: Uncomment the next line to return response Response(201, Language{}) or use other options such as http.Ok ...
	//return Response(201, Language{}), nil

	//TODO: Uncomment the next line to return response Response(400, Error{}) or use other options such as http.Ok ...
	//return Response(400, Error{}), nil

	//TODO: Uncomment the next line to return response Response(401, Error{}) or use other options such as http.Ok ...
	//return Response(401, Error{}), nil

	//TODO: Uncomment the next line to return response Response(403, Error{}) or use other options such as http.Ok ...
	//return Response(403, Error{}), nil

	//TODO: Uncomment the next line to return response Response(409, Error{}) or use other options such as http.Ok ...
	//return Response(409, Error{}), nil

	//TODO: Uncomment the next line to return response Response(500, Error{}) or use other options such as http.Ok ...
	//return Response(500, Error{}), nil

	return Response(http.StatusNotImplemented, nil), errors.New("CreateLanguage method not implemented")
}

// DeleteLanguage - Deletes a langauge.
func (s *LanguagesApiService) DeleteLanguage(ctx context.Context, id string) (ImplResponse, error) {
	// TODO - update DeleteLanguage with the required logic for this service method.
	// Add api_languages_service.go to the .openapi-generator-ignore to avoid overwriting this service implementation when updating open api generation.

	//TODO: Uncomment the next line to return response Response(204, {}) or use other options such as http.Ok ...
	//return Response(204, nil),nil

	//TODO: Uncomment the next line to return response Response(400, Error{}) or use other options such as http.Ok ...
	//return Response(400, Error{}), nil

	//TODO: Uncomment the next line to return response Response(401, Error{}) or use other options such as http.Ok ...
	//return Response(401, Error{}), nil

	//TODO: Uncomment the next line to return response Response(403, Error{}) or use other options such as http.Ok ...
	//return Response(403, Error{}), nil

	//TODO: Uncomment the next line to return response Response(404, Error{}) or use other options such as http.Ok ...
	//return Response(404, Error{}), nil

	//TODO: Uncomment the next line to return response Response(500, Error{}) or use other options such as http.Ok ...
	//return Response(500, Error{}), nil

	return Response(http.StatusNotImplemented, nil), errors.New("DeleteLanguage method not implemented")
}

// GetLanguage - Returns a language.
func (s *LanguagesApiService) GetLanguage(ctx context.Context, id string) (ImplResponse, error) {
	// TODO - update GetLanguage with the required logic for this service method.
	// Add api_languages_service.go to the .openapi-generator-ignore to avoid overwriting this service implementation when updating open api generation.

	//TODO: Uncomment the next line to return response Response(200, Language{}) or use other options such as http.Ok ...
	//return Response(200, Language{}), nil

	//TODO: Uncomment the next line to return response Response(400, Error{}) or use other options such as http.Ok ...
	//return Response(400, Error{}), nil

	//TODO: Uncomment the next line to return response Response(401, Error{}) or use other options such as http.Ok ...
	//return Response(401, Error{}), nil

	//TODO: Uncomment the next line to return response Response(403, Error{}) or use other options such as http.Ok ...
	//return Response(403, Error{}), nil

	//TODO: Uncomment the next line to return response Response(404, Error{}) or use other options such as http.Ok ...
	//return Response(404, Error{}), nil

	//TODO: Uncomment the next line to return response Response(500, Error{}) or use other options such as http.Ok ...
	//return Response(500, Error{}), nil

	return Response(http.StatusOK, StubLanguage), nil
}

// GetLanguages - Returns a list of languages.
func (s *LanguagesApiService) GetLanguages(ctx context.Context) (ImplResponse, error) {
	// TODO - update GetLanguages with the required logic for this service method.
	// Add api_languages_service.go to the .openapi-generator-ignore to avoid overwriting this service implementation when updating open api generation.

	//TODO: Uncomment the next line to return response Response(200, []Language{}) or use other options such as http.Ok ...
	//return Response(200, []Language{}), nil

	//TODO: Uncomment the next line to return response Response(401, Error{}) or use other options such as http.Ok ...
	//return Response(401, Error{}), nil

	//TODO: Uncomment the next line to return response Response(403, Error{}) or use other options such as http.Ok ...
	//return Response(403, Error{}), nil

	//TODO: Uncomment the next line to return response Response(500, Error{}) or use other options such as http.Ok ...
	//return Response(500, Error{}), nil

	list := []Language{StubLanguage}
	return Response(http.StatusOK, list), nil
}

// UpdateLanguage - Updates a langauge.
func (s *LanguagesApiService) UpdateLanguage(ctx context.Context, id string, language Language) (ImplResponse, error) {
	// TODO - update UpdateLanguage with the required logic for this service method.
	// Add api_languages_service.go to the .openapi-generator-ignore to avoid overwriting this service implementation when updating open api generation.

	//TODO: Uncomment the next line to return response Response(200, Language{}) or use other options such as http.Ok ...
	//return Response(200, Language{}), nil

	//TODO: Uncomment the next line to return response Response(400, Error{}) or use other options such as http.Ok ...
	//return Response(400, Error{}), nil

	//TODO: Uncomment the next line to return response Response(401, Error{}) or use other options such as http.Ok ...
	//return Response(401, Error{}), nil

	//TODO: Uncomment the next line to return response Response(403, Error{}) or use other options such as http.Ok ...
	//return Response(403, Error{}), nil

	//TODO: Uncomment the next line to return response Response(404, Error{}) or use other options such as http.Ok ...
	//return Response(404, Error{}), nil

	//TODO: Uncomment the next line to return response Response(409, Error{}) or use other options such as http.Ok ...
	//return Response(409, Error{}), nil

	//TODO: Uncomment the next line to return response Response(500, Error{}) or use other options such as http.Ok ...
	//return Response(500, Error{}), nil

	return Response(http.StatusNotImplemented, nil), errors.New("UpdateLanguage method not implemented")
}

