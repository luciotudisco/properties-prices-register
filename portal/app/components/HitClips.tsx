/* eslint-disable @typescript-eslint/no-explicit-any */

import { Button, Flex } from "@mantine/core";
import { useEffect, useState } from "react";
import { useInstantSearch } from "react-instantsearch";

const SearchHitClips = function (props: { hit: any }): JSX.Element {
  const { hit } = props;
  const { setIndexUiState } = useInstantSearch();
  const [propertyType, setPropertyType] = useState(null);
  const [county, setCounty] = useState(null);
  const [locality, setLocality] = useState(null);
  const [neighborhood, setNeighborhood] = useState(null);
  const [street, setStreet] = useState(null);

  useEffect(() => {
    setIndexUiState((prevIndexUiState) => ({
      ...prevIndexUiState,
      refinementList: {
        property_type: propertyType
          ? [propertyType]
          : prevIndexUiState.refinementList?.property_type || [],
        county: county
          ? [county]
          : prevIndexUiState.refinementList?.county || [],
        locality: locality
          ? [locality]
          : prevIndexUiState.refinementList?.locality || [],
        neighborhood: neighborhood
          ? [neighborhood]
          : prevIndexUiState.refinementList?.neighborhood || [],
        street: street
          ? [street]
          : prevIndexUiState.refinementList?.street || [],
      },
    }));
  }, [propertyType, county, locality, neighborhood, street]);

  return (
    <Flex
      w="full"
      gap="xs"
      justify="flex-start"
      align="flex-start"
      direction="row"
      wrap="wrap"
    >
      <Button
        variant="subtle"
        radius="xs"
        size="xs"
        p="xs"
        onClick={() => setPropertyType(hit.property_type)}
      >
        {hit.property_type}
      </Button>
      <Button
        variant="subtle"
        radius="xs"
        size="xs"
        p="xs"
        onClick={() => {
          setCounty(hit.county);
          setLocality(null);
          setNeighborhood(null);
          setStreet(null);
        }}
      >
        {hit.county}
      </Button>
      {hit.locality && (
        <Button
          variant="subtle"
          radius="xs"
          size="xs"
          p="xs"
          onClick={() => {
            setCounty(hit.county);
            setLocality(hit.locality);
            setNeighborhood(null);
            setStreet(null);
          }}
        >
          {hit.locality}
        </Button>
      )}
      {hit.neighborhood && hit.neighborhood !== hit.locality && (
        <Button
          variant="subtle"
          radius="xs"
          size="xs"
          p="xs"
          onClick={() => {
            setCounty(hit.county);
            setLocality(hit.locality);
            setNeighborhood(hit.neighborhood);
            setStreet(null);
          }}
        >
          {hit.neighborhood}
        </Button>
      )}
      {hit.street && (
        <Button
          variant="subtle"
          radius="xs"
          p="xs"
          size="xs"
          onClick={() => {
            setCounty(hit.county);
            setLocality(hit.locality);
            setNeighborhood(hit.neighborhood);
            setStreet(hit.street);
          }}
        >
          {hit.street}
        </Button>
      )}
    </Flex>
  );
};

export default SearchHitClips;
