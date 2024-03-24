import SearchBar from "./SearchBar";
import { Burger, Flex, Title } from "@mantine/core";

export interface HeaderProps {
  opened?: boolean;
  toggle: () => void;
}

const Header = function (props: HeaderProps): JSX.Element {
  const { opened, toggle } = props;
  return (
    <Flex align="center" gap="sm" className="w-full h-full px-5 flex-row">
      <Burger
        opened={opened}
        onClick={toggle}
        hiddenFrom="sm"
        size="sm"
        color="white"
      />
      <Title order={1} className="w-full text-xl text-white" visibleFrom="sm">
        Irish Properties Prices
      </Title>
      <SearchBar />
    </Flex>
  );
};

export default Header;
