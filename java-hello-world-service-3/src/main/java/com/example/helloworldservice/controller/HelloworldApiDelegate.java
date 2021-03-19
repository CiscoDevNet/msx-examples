package com.example.helloworldservice.controller;

import com.example.helloworldservice.model.Error;
import com.example.helloworldservice.model.Item;
import com.example.helloworldservice.model.Language;
import java.util.UUID;
import io.swagger.annotations.*;
import org.springframework.data.domain.Pageable;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.context.request.NativeWebRequest;
import org.springframework.web.multipart.MultipartFile;

import java.util.List;
import java.util.Map;
import java.util.Optional;

/**
 * A delegate to be called by the {@link HelloworldApiController}}.
 * Implement this interface with a {@link org.springframework.stereotype.Service} annotated class.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.SpringCodegen", date = "2021-03-16T15:42:06.037381-04:00[America/New_York]")
public interface HelloworldApiDelegate {

    default Optional<NativeWebRequest> getRequest() {
        return Optional.empty();
    }

    /**
     * POST /helloworld/api/v1/items : Creates a new Hello World item.
     *
     * @param item  (required)
     * @return Created (status code 201)
     *         or Bad Request (status code 400)
     *         or Unauthenticated (status code 401)
     *         or Unauthorized (status code 403)
     *         or Internal Server Error (status code 500)
     * @see HelloworldApi#createItem
     */
    default ResponseEntity<Item> createItem(Item item) {
        getRequest().ifPresent(request -> {
            for (MediaType mediaType: MediaType.parseMediaTypes(request.getHeader("Accept"))) {
                if (mediaType.isCompatibleWith(MediaType.valueOf("application/json"))) {
                    String exampleString = "{ \"languageId\" : \"046b6c7f-0b8a-43b9-b35d-6489e6daee91\", \"id\" : \"046b6c7f-0b8a-43b9-b35d-6489e6daee91\", \"languageName\" : \"languageName\", \"value\" : \"value\" }";
                    ApiUtil.setExampleResponse(request, "application/json", exampleString);
                    break;
                }
            }
        });
        return new ResponseEntity<>(HttpStatus.NOT_IMPLEMENTED);

    }

    /**
     * POST /helloworld/api/v1/languages : Creates a new langauge.
     *
     * @param language  (required)
     * @return Created (status code 201)
     *         or Bad Request (status code 400)
     *         or Unauthenticated (status code 401)
     *         or Unauthorized (status code 403)
     *         or Conflict (status code 409)
     *         or Internal Server Error (status code 500)
     * @see HelloworldApi#createLanguage
     */
    default ResponseEntity<Language> createLanguage(Language language) {
        getRequest().ifPresent(request -> {
            for (MediaType mediaType: MediaType.parseMediaTypes(request.getHeader("Accept"))) {
                if (mediaType.isCompatibleWith(MediaType.valueOf("application/json"))) {
                    String exampleString = "{ \"name\" : \"name\", \"description\" : \"description\", \"id\" : \"046b6c7f-0b8a-43b9-b35d-6489e6daee91\" }";
                    ApiUtil.setExampleResponse(request, "application/json", exampleString);
                    break;
                }
            }
        });
        return new ResponseEntity<>(HttpStatus.NOT_IMPLEMENTED);

    }

    /**
     * DELETE /helloworld/api/v1/items/{id} : Deletes a Hello World item.
     *
     * @param id  (required)
     * @return No Content (status code 204)
     *         or Bad Request (status code 400)
     *         or Unauthenticated (status code 401)
     *         or Unauthorized (status code 403)
     *         or Not Found (status code 404)
     *         or Internal Server Error (status code 500)
     * @see HelloworldApi#deleteItem
     */
    default ResponseEntity<Void> deleteItem(UUID id) {
        return new ResponseEntity<>(HttpStatus.NOT_IMPLEMENTED);

    }

    /**
     * DELETE /helloworld/api/v1/languages/{id} : Deletes a langauge.
     *
     * @param id  (required)
     * @return No Content (status code 204)
     *         or Bad Request (status code 400)
     *         or Unauthenticated (status code 401)
     *         or Unauthorized (status code 403)
     *         or Not Found (status code 404)
     *         or Internal Server Error (status code 500)
     * @see HelloworldApi#deleteLanguage
     */
    default ResponseEntity<Void> deleteLanguage(UUID id) {
        return new ResponseEntity<>(HttpStatus.NOT_IMPLEMENTED);

    }

    /**
     * GET /helloworld/api/v1/items/{id} : Returns a Hello World item.
     *
     * @param id  (required)
     * @return OK (status code 200)
     *         or Bad Request (status code 400)
     *         or Unauthenticated (status code 401)
     *         or Unauthorized (status code 403)
     *         or Not Found (status code 404)
     *         or Internal Server Error (status code 500)
     * @see HelloworldApi#getItem
     */
    default ResponseEntity<Item> getItem(UUID id) {
        getRequest().ifPresent(request -> {
            for (MediaType mediaType: MediaType.parseMediaTypes(request.getHeader("Accept"))) {
                if (mediaType.isCompatibleWith(MediaType.valueOf("application/json"))) {
                    String exampleString = "{ \"languageId\" : \"046b6c7f-0b8a-43b9-b35d-6489e6daee91\", \"id\" : \"046b6c7f-0b8a-43b9-b35d-6489e6daee91\", \"languageName\" : \"languageName\", \"value\" : \"value\" }";
                    ApiUtil.setExampleResponse(request, "application/json", exampleString);
                    break;
                }
            }
        });
        return new ResponseEntity<>(HttpStatus.NOT_IMPLEMENTED);

    }

    /**
     * GET /helloworld/api/v1/items : Returns a list of Hello World items.
     *
     * @param languageId  (optional)
     * @return OK (status code 200)
     *         or Bad Request (status code 400)
     *         or Unauthenticated (status code 401)
     *         or Unauthorized (status code 403)
     *         or Internal Server Error (status code 500)
     * @see HelloworldApi#getItems
     */
    default ResponseEntity<List<Item>> getItems(UUID languageId) {
        getRequest().ifPresent(request -> {
            for (MediaType mediaType: MediaType.parseMediaTypes(request.getHeader("Accept"))) {
                if (mediaType.isCompatibleWith(MediaType.valueOf("application/json"))) {
                    String exampleString = "{ \"languageId\" : \"046b6c7f-0b8a-43b9-b35d-6489e6daee91\", \"id\" : \"046b6c7f-0b8a-43b9-b35d-6489e6daee91\", \"languageName\" : \"languageName\", \"value\" : \"value\" }";
                    ApiUtil.setExampleResponse(request, "application/json", exampleString);
                    break;
                }
            }
        });
        return new ResponseEntity<>(HttpStatus.NOT_IMPLEMENTED);

    }

    /**
     * GET /helloworld/api/v1/languages/{id} : Returns a language.
     *
     * @param id  (required)
     * @return OK (status code 200)
     *         or Bad Request (status code 400)
     *         or Unauthenticated (status code 401)
     *         or Unauthorized (status code 403)
     *         or Not Found (status code 404)
     *         or Internal Server Error (status code 500)
     * @see HelloworldApi#getLanguage
     */
    default ResponseEntity<Language> getLanguage(UUID id) {
        getRequest().ifPresent(request -> {
            for (MediaType mediaType: MediaType.parseMediaTypes(request.getHeader("Accept"))) {
                if (mediaType.isCompatibleWith(MediaType.valueOf("application/json"))) {
                    String exampleString = "{ \"name\" : \"name\", \"description\" : \"description\", \"id\" : \"046b6c7f-0b8a-43b9-b35d-6489e6daee91\" }";
                    ApiUtil.setExampleResponse(request, "application/json", exampleString);
                    break;
                }
            }
        });
        return new ResponseEntity<>(HttpStatus.NOT_IMPLEMENTED);

    }

    /**
     * GET /helloworld/api/v1/languages : Returns a list of languages.
     *
     * @return OK (status code 200)
     *         or Unauthenticated (status code 401)
     *         or Unauthorized (status code 403)
     *         or Internal Server Error (status code 500)
     * @see HelloworldApi#getLanguages
     */
    default ResponseEntity<List<Language>> getLanguages() {
        getRequest().ifPresent(request -> {
            for (MediaType mediaType: MediaType.parseMediaTypes(request.getHeader("Accept"))) {
                if (mediaType.isCompatibleWith(MediaType.valueOf("application/json"))) {
                    String exampleString = "{ \"name\" : \"name\", \"description\" : \"description\", \"id\" : \"046b6c7f-0b8a-43b9-b35d-6489e6daee91\" }";
                    ApiUtil.setExampleResponse(request, "application/json", exampleString);
                    break;
                }
            }
        });
        return new ResponseEntity<>(HttpStatus.NOT_IMPLEMENTED);

    }

    /**
     * PUT /helloworld/api/v1/items/{id} : Updates a Hello World item.
     *
     * @param id  (required)
     * @param item  (required)
     * @return OK (status code 200)
     *         or Bad Request (status code 400)
     *         or Unauthenticated (status code 401)
     *         or Unauthorized (status code 403)
     *         or Not Found (status code 404)
     *         or Internal Server Error (status code 500)
     * @see HelloworldApi#updateItem
     */
    default ResponseEntity<Item> updateItem(UUID id,
        Item item) {
        getRequest().ifPresent(request -> {
            for (MediaType mediaType: MediaType.parseMediaTypes(request.getHeader("Accept"))) {
                if (mediaType.isCompatibleWith(MediaType.valueOf("application/json"))) {
                    String exampleString = "{ \"languageId\" : \"046b6c7f-0b8a-43b9-b35d-6489e6daee91\", \"id\" : \"046b6c7f-0b8a-43b9-b35d-6489e6daee91\", \"languageName\" : \"languageName\", \"value\" : \"value\" }";
                    ApiUtil.setExampleResponse(request, "application/json", exampleString);
                    break;
                }
            }
        });
        return new ResponseEntity<>(HttpStatus.NOT_IMPLEMENTED);

    }

    /**
     * PUT /helloworld/api/v1/languages/{id} : Updates a langauge.
     *
     * @param id  (required)
     * @param language  (required)
     * @return OK (status code 200)
     *         or Bad Request (status code 400)
     *         or Unauthenticated (status code 401)
     *         or Unauthorized (status code 403)
     *         or Not Found (status code 404)
     *         or Conflict (status code 409)
     *         or Internal Server Error (status code 500)
     * @see HelloworldApi#updateLanguage
     */
    default ResponseEntity<Language> updateLanguage(UUID id,
        Language language) {
        getRequest().ifPresent(request -> {
            for (MediaType mediaType: MediaType.parseMediaTypes(request.getHeader("Accept"))) {
                if (mediaType.isCompatibleWith(MediaType.valueOf("application/json"))) {
                    String exampleString = "{ \"name\" : \"name\", \"description\" : \"description\", \"id\" : \"046b6c7f-0b8a-43b9-b35d-6489e6daee91\" }";
                    ApiUtil.setExampleResponse(request, "application/json", exampleString);
                    break;
                }
            }
        });
        return new ResponseEntity<>(HttpStatus.NOT_IMPLEMENTED);

    }

}
