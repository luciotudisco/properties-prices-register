import { Button, Flex, Text } from "@mantine/core";
import { useEffect, useState } from "react";
import Lottie from "react-lottie-player";
import { useInstantSearch } from "react-instantsearch";

const EmptyHits = function (): JSX.Element {
  const { setIndexUiState } = useInstantSearch();
  const [animationData, setAnimationData] = useState<object>();

  useEffect(() => {
    import("./assets/no-results-lottie.json").then(setAnimationData);
  }, []);

  function clearFilters() {
    setIndexUiState((prevIndexUiState) => ({
      ...prevIndexUiState,
      query: "",
      refinementList: {},
    }));
  }

  return (
    <Flex
      direction="column"
      align="center"
      justify="center"
      w="100%"
      h="100%"
      gap="md"
    >
      <Lottie animationData={animationData} loop play />
      <Text size="sm">No results found</Text>
      <Button variant="subtle" onClick={clearFilters}>
        Clear Filters
      </Button>
    </Flex>
  );
};

export default EmptyHits;
