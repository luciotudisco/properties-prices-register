import { useRefinementList } from "react-instantsearch";
import "instantsearch.css/themes/satellite.css";
import { Button, Checkbox, Flex, Input, Text } from "@mantine/core";
import { IconSearch } from "@tabler/icons-react";

const SearchFilter = function (props: {
  attribute: string;
  label: string;
  searchable: boolean;
  limit: number;
  showMoreLimit?: number;
}): JSX.Element {
  const { label, searchable } = props;
  const {
    items,
    refine,
    searchForItems,
    toggleShowMore,
    isShowingMore,
    hasExhaustiveItems,
  } = useRefinementList(props);

  return (
    <Flex
      gap="xs"
      direction="column"
      className="border m-2 border-slate-100-500"
    >
      <Flex
        gap="xs"
        direction="column"
        className="min-h-8 bg-slate-900  align-middle justify-center"
      >
        <Text size="xs" className="uppercase text-white p-2">
          {label}
        </Text>
      </Flex>
      <Flex gap="xs" direction="column" className="p-2">
        <Input
          type="search"
          display={searchable ? "block" : "none"}
          onChange={(event) => searchForItems(event.currentTarget.value)}
          leftSection={<IconSearch size={16} />}
          rightSectionPointerEvents="all"
          size="xs"
        />
        {items.map((item) => (
          <Flex gap="xs" direction="row" align="center">
            <Checkbox
              checked={item.isRefined}
              onChange={() => refine(item.value)}
              size="xs"
              className="text-sm"
            />
            <Text size="xs" className="text-xs w-full">
              {item.label}
            </Text>
            <Text size="xs" className="text-xs">
              {item.count}
            </Text>
          </Flex>
        ))}
        {!hasExhaustiveItems && (
          <Button
            onClick={toggleShowMore}
            variant="transparent"
            className="text-slate-400"
          >
            {isShowingMore ? "Show less" : "Show more"}
          </Button>
        )}
      </Flex>
    </Flex>
  );
};

export default SearchFilter;
