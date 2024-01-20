import type { Metadata } from "next";
import "./globals.css";
import Footer from "./components/Footer";
import Header from "./components/Header";

export const metadata: Metadata = {
  title: "Properties Prices Register",
  description: "Properties Prices Register",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="flex flex-col h-screen">
        <nav className="h-14">
          <Header />
        </nav>
        <main className="flex-1 overflow-y-auto">{children}</main>
        <footer className="h-10 w-full">
          <Footer />
        </footer>
      </body>
    </html>
  );
}
