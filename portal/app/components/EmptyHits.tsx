import { Flex, Text } from "@mantine/core";
import { useEffect, useState } from "react";
import Lottie from "react-lottie-player";
import ClearFilters from "./ClearFilters";

const EmptyHits = function (): JSX.Element {
  const [animationData, setAnimationData] = useState<object>();

  useEffect(() => {
    import("./assets/no-results-lottie.json").then(setAnimationData);
  }, []);

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
      <ClearFilters />
    </Flex>
  );
};

export default EmptyHits;
