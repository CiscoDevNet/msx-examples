/**
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech) (5.0.1).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */
package com.example.helloworldservice.controller;

import com.example.helloworldservice.model.Error;
import com.example.helloworldservice.model.Item;
import com.example.helloworldservice.model.Language;
import java.util.UUID;
import io.swagger.annotations.*;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.data.domain.Pageable;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;
import springfox.documentation.annotations.ApiIgnore;

import javax.validation.Valid;
import javax.validation.constraints.*;
import java.util.List;
import java.util.Map;
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.SpringCodegen", date = "2021-03-16T15:42:06.037381-04:00[America/New_York]")
@Validated
@Api(value = "helloworld", description = "the helloworld API")
public interface HelloworldApi {

    default HelloworldApiDelegate getDelegate() {
        return new HelloworldApiDelegate() {};
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
     */
    @ApiOperation(value = "Creates a new Hello World item.", nickname = "createItem", notes = "", response = Item.class, tags={ "Items", })
    @ApiResponses(value = { 
        @ApiResponse(code = 201, message = "Created", response = Item.class),
        @ApiResponse(code = 400, message = "Bad Request", response = Error.class),
        @ApiResponse(code = 401, message = "Unauthenticated", response = Error.class),
        @ApiResponse(code = 403, message = "Unauthorized", response = Error.class),
        @ApiResponse(code = 500, message = "Internal Server Error", response = Error.class) })
    @PostMapping(
        value = "/helloworld/api/v1/items",
        produces = { "application/json" },
        consumes = { "application/json" }
    )
    default ResponseEntity<Item> createItem(@ApiParam(value = "" ,required=true )  @Valid @RequestBody Item item) {
        return getDelegate().createItem(item);
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
     */
    @ApiOperation(value = "Creates a new langauge.", nickname = "createLanguage", notes = "", response = Language.class, tags={ "Languages", })
    @ApiResponses(value = { 
        @ApiResponse(code = 201, message = "Created", response = Language.class),
        @ApiResponse(code = 400, message = "Bad Request", response = Error.class),
        @ApiResponse(code = 401, message = "Unauthenticated", response = Error.class),
        @ApiResponse(code = 403, message = "Unauthorized", response = Error.class),
        @ApiResponse(code = 409, message = "Conflict", response = Error.class),
        @ApiResponse(code = 500, message = "Internal Server Error", response = Error.class) })
    @PostMapping(
        value = "/helloworld/api/v1/languages",
        produces = { "application/json" },
        consumes = { "application/json" }
    )
    default ResponseEntity<Language> createLanguage(@ApiParam(value = "" ,required=true )  @Valid @RequestBody Language language) {
        return getDelegate().createLanguage(language);
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
     */
    @ApiOperation(value = "Deletes a Hello World item.", nickname = "deleteItem", notes = "", tags={ "Items", })
    @ApiResponses(value = { 
        @ApiResponse(code = 204, message = "No Content"),
        @ApiResponse(code = 400, message = "Bad Request", response = Error.class),
        @ApiResponse(code = 401, message = "Unauthenticated", response = Error.class),
        @ApiResponse(code = 403, message = "Unauthorized", response = Error.class),
        @ApiResponse(code = 404, message = "Not Found", response = Error.class),
        @ApiResponse(code = 500, message = "Internal Server Error", response = Error.class) })
    @DeleteMapping(
        value = "/helloworld/api/v1/items/{id}",
        produces = { "application/json" }
    )
    default ResponseEntity<Void> deleteItem(@ApiParam(value = "",required=true) @PathVariable("id") UUID id) {
        return getDelegate().deleteItem(id);
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
     */
    @ApiOperation(value = "Deletes a langauge.", nickname = "deleteLanguage", notes = "", tags={ "Languages", })
    @ApiResponses(value = { 
        @ApiResponse(code = 204, message = "No Content"),
        @ApiResponse(code = 400, message = "Bad Request", response = Error.class),
        @ApiResponse(code = 401, message = "Unauthenticated", response = Error.class),
        @ApiResponse(code = 403, message = "Unauthorized", response = Error.class),
        @ApiResponse(code = 404, message = "Not Found", response = Error.class),
        @ApiResponse(code = 500, message = "Internal Server Error", response = Error.class) })
    @DeleteMapping(
        value = "/helloworld/api/v1/languages/{id}",
        produces = { "application/json" }
    )
    default ResponseEntity<Void> deleteLanguage(@ApiParam(value = "",required=true) @PathVariable("id") UUID id) {
        return getDelegate().deleteLanguage(id);
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
     */
    @ApiOperation(value = "Returns a Hello World item.", nickname = "getItem", notes = "", response = Item.class, tags={ "Items", })
    @ApiResponses(value = { 
        @ApiResponse(code = 200, message = "OK", response = Item.class),
        @ApiResponse(code = 400, message = "Bad Request", response = Error.class),
        @ApiResponse(code = 401, message = "Unauthenticated", response = Error.class),
        @ApiResponse(code = 403, message = "Unauthorized", response = Error.class),
        @ApiResponse(code = 404, message = "Not Found", response = Error.class),
        @ApiResponse(code = 500, message = "Internal Server Error", response = Error.class) })
    @GetMapping(
        value = "/helloworld/api/v1/items/{id}",
        produces = { "application/json" }
    )
    default ResponseEntity<Item> getItem(@ApiParam(value = "",required=true) @PathVariable("id") UUID id) {
        return getDelegate().getItem(id);
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
     */
    @ApiOperation(value = "Returns a list of Hello World items.", nickname = "getItems", notes = "", response = Item.class, responseContainer = "List", tags={ "Items", })
    @ApiResponses(value = { 
        @ApiResponse(code = 200, message = "OK", response = Item.class, responseContainer = "List"),
        @ApiResponse(code = 400, message = "Bad Request", response = Error.class),
        @ApiResponse(code = 401, message = "Unauthenticated", response = Error.class),
        @ApiResponse(code = 403, message = "Unauthorized", response = Error.class),
        @ApiResponse(code = 500, message = "Internal Server Error", response = Error.class) })
    @GetMapping(
        value = "/helloworld/api/v1/items",
        produces = { "application/json" }
    )
    default ResponseEntity<List<Item>> getItems(@ApiParam(value = "") @Valid @RequestParam(value = "languageId", required = false) UUID languageId) {
        return getDelegate().getItems(languageId);
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
     */
    @ApiOperation(value = "Returns a language.", nickname = "getLanguage", notes = "", response = Language.class, tags={ "Languages", })
    @ApiResponses(value = { 
        @ApiResponse(code = 200, message = "OK", response = Language.class),
        @ApiResponse(code = 400, message = "Bad Request", response = Error.class),
        @ApiResponse(code = 401, message = "Unauthenticated", response = Error.class),
        @ApiResponse(code = 403, message = "Unauthorized", response = Error.class),
        @ApiResponse(code = 404, message = "Not Found", response = Error.class),
        @ApiResponse(code = 500, message = "Internal Server Error", response = Error.class) })
    @GetMapping(
        value = "/helloworld/api/v1/languages/{id}",
        produces = { "application/json" }
    )
    default ResponseEntity<Language> getLanguage(@ApiParam(value = "",required=true) @PathVariable("id") UUID id) {
        return getDelegate().getLanguage(id);
    }


    /**
     * GET /helloworld/api/v1/languages : Returns a list of languages.
     *
     * @return OK (status code 200)
     *         or Unauthenticated (status code 401)
     *         or Unauthorized (status code 403)
     *         or Internal Server Error (status code 500)
     */
    @ApiOperation(value = "Returns a list of languages.", nickname = "getLanguages", notes = "", response = Language.class, responseContainer = "List", tags={ "Languages", })
    @ApiResponses(value = { 
        @ApiResponse(code = 200, message = "OK", response = Language.class, responseContainer = "List"),
        @ApiResponse(code = 401, message = "Unauthenticated", response = Error.class),
        @ApiResponse(code = 403, message = "Unauthorized", response = Error.class),
        @ApiResponse(code = 500, message = "Internal Server Error", response = Error.class) })
    @GetMapping(
        value = "/helloworld/api/v1/languages",
        produces = { "application/json" }
    )
    default ResponseEntity<List<Language>> getLanguages() {
        return getDelegate().getLanguages();
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
     */
    @ApiOperation(value = "Updates a Hello World item.", nickname = "updateItem", notes = "", response = Item.class, tags={ "Items", })
    @ApiResponses(value = { 
        @ApiResponse(code = 200, message = "OK", response = Item.class),
        @ApiResponse(code = 400, message = "Bad Request", response = Error.class),
        @ApiResponse(code = 401, message = "Unauthenticated", response = Error.class),
        @ApiResponse(code = 403, message = "Unauthorized", response = Error.class),
        @ApiResponse(code = 404, message = "Not Found", response = Error.class),
        @ApiResponse(code = 500, message = "Internal Server Error", response = Error.class) })
    @PutMapping(
        value = "/helloworld/api/v1/items/{id}",
        produces = { "application/json" },
        consumes = { "application/json" }
    )
    default ResponseEntity<Item> updateItem(@ApiParam(value = "",required=true) @PathVariable("id") UUID id,@ApiParam(value = "" ,required=true )  @Valid @RequestBody Item item) {
        return getDelegate().updateItem(id, item);
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
     */
    @ApiOperation(value = "Updates a langauge.", nickname = "updateLanguage", notes = "", response = Language.class, tags={ "Languages", })
    @ApiResponses(value = { 
        @ApiResponse(code = 200, message = "OK", response = Language.class),
        @ApiResponse(code = 400, message = "Bad Request", response = Error.class),
        @ApiResponse(code = 401, message = "Unauthenticated", response = Error.class),
        @ApiResponse(code = 403, message = "Unauthorized", response = Error.class),
        @ApiResponse(code = 404, message = "Not Found", response = Error.class),
        @ApiResponse(code = 409, message = "Conflict", response = Error.class),
        @ApiResponse(code = 500, message = "Internal Server Error", response = Error.class) })
    @PutMapping(
        value = "/helloworld/api/v1/languages/{id}",
        produces = { "application/json" },
        consumes = { "application/json" }
    )
    default ResponseEntity<Language> updateLanguage(@ApiParam(value = "",required=true) @PathVariable("id") UUID id,@ApiParam(value = "" ,required=true )  @Valid @RequestBody Language language) {
        return getDelegate().updateLanguage(id, language);
    }

}
