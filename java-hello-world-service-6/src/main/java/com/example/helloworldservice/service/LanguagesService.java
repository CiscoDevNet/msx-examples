//
// Copyright (c) 2021 Cisco Systems, Inc and its affiliates
// All Rights reserved
//
package com.example.helloworldservice.service;

import com.cisco.msx.security.SecurityContextBasedRBACUtils;
import com.cisco.msx.security.SecurityContextDetails;
import com.example.helloworldservice.cockroach.model.LanguageRow;
import com.example.helloworldservice.cockroach.repository.LanguagesRepository;
import com.example.helloworldservice.model.Language;

import java.util.List;
import java.util.UUID;
import java.util.stream.Collectors;

import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;


@RequiredArgsConstructor
public class LanguagesService {
    @Autowired
    private SecurityContextBasedRBACUtils securityContextBasedRBACUtils;

    private final LanguagesRepository languagesRepository;

    public Language saveLanguage(Language language) {
        // Convert from DTO to model to prepare for saving.
        LanguageRow languageRow = LanguageItemConverter.convert(language);

        // Cave to database.
        LanguageRow savedLanguageRow = languagesRepository.save(languageRow);

        // Convert into DTO for response.
        Language savedLanguage = LanguageItemConverter.convert(savedLanguageRow);

        return savedLanguage;
    }

    protected LanguageRow getRawLanguage(UUID languageId) {
        // Get record from database.
        LanguageRow languageRow = languagesRepository.getOne(languageId);
        return languageRow;
    }

    public Language getLanguage(UUID languageId) {
        // Get record from database.
        LanguageRow languageRow = getRawLanguage(languageId);

        // Convert into DTO for response.
        Language language = LanguageItemConverter.convert(languageRow);

        return language;
    }

    public List<Language> getAllLanguages() {
        SecurityContextDetails securityContextDetails = securityContextBasedRBACUtils.getSecurityContextDetails();
        // TODO - Do something with the security context.

        // Get records from database.
        List<LanguageRow> languageRows = languagesRepository.findAll();

        // Convert into DTO for response.
        List<Language> languages = languageRows.stream()
                .map(LanguageItemConverter::convert)
                .collect(Collectors.toList());

        return languages;
    }

    public Language updateLanguage(UUID languageId, Language language) {
        // Will throw exception if language entry does not exist.
        LanguageRow existingLanguageRow = languagesRepository.getOne(languageId);

        // Convert the DTO into the domain model.
        LanguageRow languageRow = LanguageItemConverter.convert(language);

        // Set greetingId to overwrite existing record.
        languageRow.setLanguageId(languageId);

        // Save domain model object.
        LanguageRow savedLanguageRow = languagesRepository.save(languageRow);

        // Convert domain model to DTO in preparation for response.
        Language savedLanguage = LanguageItemConverter.convert(savedLanguageRow);

        return savedLanguage;
    }

    public void deleteLanguage(UUID languageId) {
        languagesRepository.deleteById(languageId);
    }
}
