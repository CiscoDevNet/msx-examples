package com.example.helloworldservice.model;

import java.util.Objects;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonCreator;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.util.UUID;
import org.openapitools.jackson.nullable.JsonNullable;
import javax.validation.Valid;
import javax.validation.constraints.*;

/**
 * Item
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.SpringCodegen", date = "2021-03-16T15:42:06.037381-04:00[America/New_York]")
public class Item   {
  @JsonProperty("id")
  private UUID id;

  @JsonProperty("languageId")
  private UUID languageId;

  @JsonProperty("languageName")
  private String languageName;

  @JsonProperty("value")
  private String value;

  public Item id(UUID id) {
    this.id = id;
    return this;
  }

  /**
   * Get id
   * @return id
  */
  @ApiModelProperty(readOnly = true, value = "")

  @Valid

  public UUID getId() {
    return id;
  }

  public void setId(UUID id) {
    this.id = id;
  }

  public Item languageId(UUID languageId) {
    this.languageId = languageId;
    return this;
  }

  /**
   * Get languageId
   * @return languageId
  */
  @ApiModelProperty(required = true, value = "")
  @NotNull

  @Valid

  public UUID getLanguageId() {
    return languageId;
  }

  public void setLanguageId(UUID languageId) {
    this.languageId = languageId;
  }

  public Item languageName(String languageName) {
    this.languageName = languageName;
    return this;
  }

  /**
   * Get languageName
   * @return languageName
  */
  @ApiModelProperty(readOnly = true, value = "")


  public String getLanguageName() {
    return languageName;
  }

  public void setLanguageName(String languageName) {
    this.languageName = languageName;
  }

  public Item value(String value) {
    this.value = value;
    return this;
  }

  /**
   * Get value
   * @return value
  */
  @ApiModelProperty(required = true, value = "")
  @NotNull

@Size(min=2,max=128) 
  public String getValue() {
    return value;
  }

  public void setValue(String value) {
    this.value = value;
  }


  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Item item = (Item) o;
    return Objects.equals(this.id, item.id) &&
        Objects.equals(this.languageId, item.languageId) &&
        Objects.equals(this.languageName, item.languageName) &&
        Objects.equals(this.value, item.value);
  }

  @Override
  public int hashCode() {
    return Objects.hash(id, languageId, languageName, value);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Item {\n");
    
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    languageId: ").append(toIndentedString(languageId)).append("\n");
    sb.append("    languageName: ").append(toIndentedString(languageName)).append("\n");
    sb.append("    value: ").append(toIndentedString(value)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }
}

