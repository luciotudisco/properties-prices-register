import { Button, SimpleGrid, Text } from "@mantine/core";
import { useInfiniteHits, useStats } from "react-instantsearch";
import Hit from "./Hit";

const Hits = function (): JSX.Element {
  const { hits, showMore, isLastPage } = useInfiniteHits();
  const { nbHits } = useStats();

  return (
    <>
      <Text
        className="text-gray-400 mb-2 text-center"
        variant="caption"
        size="xs"
      >
        {nbHits} results found
      </Text>
      <SimpleGrid cols={1} spacing={2}>
        {hits.map((hit) => (
          <Hit key={hit.objectID} hit={hit} />
        ))}
        {!isLastPage && (
          <Button onClick={showMore} variant="light" size="xs" m="xs">
            Show more
          </Button>
        )}
      </SimpleGrid>
    </>
  );
};

export default Hits;
